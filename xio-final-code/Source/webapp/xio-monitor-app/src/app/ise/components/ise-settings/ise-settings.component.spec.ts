import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseSettingsComponent } from './ise-settings.component';

describe('IseSettingsComponent', () => {
  let component: IseSettingsComponent;
  let fixture: ComponentFixture<IseSettingsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseSettingsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseSettingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
